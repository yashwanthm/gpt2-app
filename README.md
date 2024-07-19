Convert to vino or onnx using 
omz_converter --name gpt-2

You would have gpt-2.bin and gpt-2.xml files in the public directory, along with gpt-2.onnx


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

## 
