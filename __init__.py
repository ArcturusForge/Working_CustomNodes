# Made by Davemane42#0042 for ComfyUI
# Updated by Arcturus: 16/05/2024

import os
import subprocess
import importlib.util
import sys
import __main__

from .MultiLatentComposite import MultiLatentComposite
from .MultiAreaConditioning import MultiAreaConditioning
from .ConditioningUpscale import ConditioningUpscale
from .ConditioningStretch import ConditioningStretch
from .ConditioningDebug import ConditioningDebug

python = sys.executable

def is_installed(package, package_overwrite=None):
    try:
        spec = importlib.util.find_spec(package)
    except ModuleNotFoundError:
        pass

    package = package_overwrite or package

    if spec is None:
        print(f"Installing {package}...")
        command = f'"{python}" -m pip install {package}'
  
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, env=os.environ)

        if result.returncode != 0:
            print(f"Couldn't install\nCommand: {command}\nError code: {result.returncode}")

NODE_CLASS_MAPPINGS = {
    MultiLatentComposite.NAME : MultiLatentComposite,
    MultiAreaConditioning.NAME : MultiAreaConditioning,
    ConditioningUpscale.NAME : ConditioningUpscale,
    ConditioningStretch.NAME : ConditioningStretch,
    ConditioningDebug.NAME : ConditioningDebug,
}

print('\033[34mDavemane42 Custom Nodes: \033[92mLoaded\033[0m')