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

## Serve the model
Dashboard > Data Science Projects > Select Project > Select Models tab > Add Model Server
Select runtime as OpenVINO Model Server, Select Make deployed models available through an external route, Unselect Require token authentication
Notice the model server created and available
Now, select Deploy Model
Name - gpt_ir
Model Framework - openvino_ir - opset1
Model Location
  - Use existing data connection
  - Name - My Storage
  - Path - models/gpt2_ir


Check the logs at OpenShift Console > Admin > Workloads > Pods > find the server name here > Logs > 
