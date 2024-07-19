## Create a project

Create a Data Connection to store the model
Add https://github.com/cfchase/basic-kserve-vllm/blob/main/setup/setup-s3.yaml to your cluster - Verify for sandbox
This adds a data connection to your project - Dashboard>Project>Data Connection - Notice My Storage and Pipeline Artifacts get added 

## Convert and Upload model

Now create a workbench RHOAI Dashboard > Data Science Projects > Create Workbench
While creating the workbench,
  - Select "Use a data connection"
  - Use existing data connection
  - On the data connection dropdown, select My Storage
Wait for the workbench to start and open the workbench
Now, download this file https://github.com/cfchase/basic-kserve-vllm/blob/main/1_download_save.ipynb and uplaod it to JupyterLab once it opens
  - Run the Download and Convert to ONXX Model block, notice the gpt2-onnx folder get created
  - Convert to IR, notice the gpt2_ir folder get created with gpt2.xml and gpt2.bin files
  - Load the helper functions to upload
  - Upload gpt2-onnx and gpt2_ir

## Create model server
Dashboard > Data Science Projects > Select Project > Select Models tab > Add Model Server
Select runtime as OpenVINO Model Server, Select Make deployed models available through an external route, Unselect Require token authentication
Notice the model server created and available

## Serve the model
Now, select Deploy Model option on the newly created server
Name - gpt_ir
Model Framework - openvino_ir - opset1
Model Location
  - Use existing data connection
  - Name - My Storage
  - Path - models/gpt2_ir


Check the logs at OpenShift Console > Admin > Workloads > Pods > find the server name here > Logs > 



# Create a Model Archive to serve with torchserve

gpt2_handler.py

```
from ts.torch_handler.base_handler import BaseHandler
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch


class GPT2Handler(BaseHandler):
    def initialize(self, context):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model_dir = context.system_properties.get("model_dir")
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
        self.model = GPT2LMHeadModel.from_pretrained(model_dir)
        self.model.to(self.device)
        self.model.eval()

    def preprocess(self, data):
        input_text = data[0].get("data") or data[0].get("body")
        inputs = self.tokenizer(input_text, return_tensors="pt")
        return inputs

    def inference(self, inputs):
        inputs = {key: val.to(self.device) for key, val in inputs.items()}
        outputs = self.model.generate(**inputs)
        return outputs

    def postprocess(self, inference_output):
        output_text = self.tokenizer.decode(inference_output[0], skip_special_tokens=True)
        return [output_text]
```
```
torch-model-archiver --model-name gpt2 --version 1.0 --serialized-file gpt2/pytorch_model.bin --handler gpt2_handler.py --extra-files "gpt2/config.json,gpt2/vocab.json,gpt2/merges.txt" --export-path gpt2mar
```
