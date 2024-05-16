from nodes import MAX_RESOLUTION

class ConditioningStretch:
    NAME = "ConditioningStretch"
    CATEGORY = "Davemane42"
    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("Conditioning",)
    FUNCTION = "upscale"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", ),
                "resolutionX": ("INT", {"default": 512, "min": 64, "max": MAX_RESOLUTION, "step": 64}),
                "resolutionY": ("INT", {"default": 512, "min": 64, "max": MAX_RESOLUTION, "step": 64}),
                "newWidth": ("INT", {"default": 512, "min": 64, "max": MAX_RESOLUTION, "step": 64}),
                "newHeight": ("INT", {"default": 512, "min": 64, "max": MAX_RESOLUTION, "step": 64}),
                #"scalar": ("INT", {"default": 2, "min": 1, "max": 100, "step": 0.5}),
            },
        }

    def upscale(self, conditioning, resolutionX, resolutionY, newWidth, newHeight, scalar=1):
        c = []
        for t in conditioning:

            n = [t[0], t[1].copy()]
            if 'area' in n[1]:

                newWidth *= scalar
                newHeight *= scalar
                
                #n[1]['area'] = tuple(map(lambda x: ((x*scalar + 32) >> 6) << 6, n[1]['area']))
                x = ((n[1]['area'][3]*8)*newWidth/resolutionX) // 8
                y = ((n[1]['area'][2]*8)*newHeight/resolutionY) // 8
                w = ((n[1]['area'][1]*8)*newWidth/resolutionX) // 8
                h = ((n[1]['area'][0]*8)*newHeight/resolutionY) // 8

                n[1]['area'] = tuple(map(lambda x: (((int(x) + 7) >> 3) << 3), [h, w, y, x]))

            c.append(n)

        return (c, )
