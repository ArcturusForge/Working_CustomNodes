class ConditioningDebug:
    NAME = "ConditioningDebug"
    CATEGORY = "Davemane42"
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "debug"
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", ),
            }
        }

    def debug(self, conditioning):
        print("\nDebug")
        for i, t in enumerate(conditioning):
            print(f"{i}:")
            if "area" in t[1]:
                print(f"\tx{t[1]['area'][3]*8} y{t[1]['area'][2]*8} \n\tw{t[1]['area'][1]*8} h{t[1]['area'][0]*8} \n\tstrength: {t[1]['strength']}")
            else:
                print(f"\tFullscreen")

        return (None, )