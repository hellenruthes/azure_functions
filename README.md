# azure
To develop locally 
1. Install Azure Functions Core Tools
Links:
-Install Azure Functions Core Tools:
https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python#install-the-azure-functions-core-tools


-Install Azurite (local storage emulator):
You can do direcly on VS Code as well
https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python

-Install Azure Storage Explorer: https://azure.microsoft.com/en-us/pro...

-DataEngineeringWithNick Azure Functions code repo:  https://github.com/DataEngineeringWit...

ref https://www.youtube.com/watch?v=I-kodc4bs4I

Commands
start project ```func init MyFunctionProject --python -m v2```
cd ```MyFunctionProject```
create virtual env ```python -m venv .venv```
activate .venv ```source .venv/bin/activate```

create function

```func start```

ctlr + c to stop
