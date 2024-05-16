class ConditioningUpscale:
    NAME = "ConditioningUpscale"
    CATEGORY = "Davemane42"
    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("Conditioning",)
    FUNCTION = "upscale"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", ),
                "scalar": ("INT", {"default": 2, "min": 1, "max": 100, "step": 0.5}),
            },
        }

    def upscale(self, conditioning, scalar):
        c = []
        for t in conditioning:

            n = [t[0], t[1].copy()]
            if 'area' in n[1]:
                
                n[1]['area'] = tuple(map(lambda x: ((x*scalar + 7) >> 3) << 3, n[1]['area']))

            c.append(n)

        return (c, )