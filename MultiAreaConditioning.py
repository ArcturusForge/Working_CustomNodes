# Made by Davemane42#0042 for ComfyUI
# 02/04/2023
# Updated by Arcturus: 16/05/2024

import torch

class MultiAreaConditioning:
    NAME = "MultiAreaConditioning"
    CATEGORY = "Davemane42"
    RETURN_TYPES = ("CONDITIONING", "INT", "INT")
    RETURN_NAMES = ("Conditioning", "resolutionX", "resolutionY")
    FUNCTION = "doStuff"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "conditioning0": ("CONDITIONING", ),
                "conditioning1": ("CONDITIONING", )
            },
            "hidden": {"extra_pnginfo": "EXTRA_PNGINFO", "unique_id": "UNIQUE_ID"},
        }

    def doStuff(self, extra_pnginfo, unique_id, **kwargs):

        c = []
        values = []
        resolutionX = 512
        resolutionY = 512

        for node in extra_pnginfo["workflow"]["nodes"]:
            if node["id"] == int(unique_id):
                values = node["properties"]["values"]
                resolutionX = node["properties"]["width"]
                resolutionY = node["properties"]["height"]
                break
        k = 0
        for arg in kwargs:
            if k > len(values): break;
            if not torch.is_tensor(kwargs[arg][0][0]): continue;

            x, y = values[k][0], values[k][1]
            w, h = values[k][2], values[k][3]

            # If fullscreen
            if (x == 0 and y == 0 and w == resolutionX and h == resolutionY):
                for t in kwargs[arg]:
                    c.append(t)
                k += 1
                continue

            if x+w > resolutionX:
                w = max(0, resolutionX-x)

            if y+h > resolutionY:
                h = max(0, resolutionY-y)

            if w == 0 or h == 0: continue;

            for t in kwargs[arg]:
                n = [t[0], t[1].copy()]
                n[1]['area'] = (h // 8, w // 8, y // 8, x // 8)
                n[1]['strength'] = values[k][4]
                n[1]['min_sigma'] = 0.0
                n[1]['max_sigma'] = 99.0

                c.append(n)

            k += 1


        return (c, resolutionX, resolutionY)
