class Solution:
    def originalDigits(self, s: str) -> str:
        
        count_dct = collections.Counter(s)
        num_dict = {}
        
        num_dict["0"] = count_dct["z"]
        num_dict["2"] = count_dct["w"]
        num_dict["4"] = count_dct["u"]
        num_dict["6"] = count_dct["x"]
        num_dict["8"] = count_dct["g"]
        
        num_dict["3"] = count_dct["h"] - num_dict["8"]
        num_dict["5"] = count_dct["f"] - num_dict["4"]
        num_dict["7"] = count_dct["s"] - num_dict["6"]
        
        num_dict["9"] = count_dct["i"] - num_dict["5"] - num_dict["6"] - num_dict["8"]
        
        num_dict["1"] = count_dct["n"] - num_dict["7"] - (2*num_dict["9"])
        
        
        return "".join(x*num_dict[x] for x in sorted(num_dict.keys()))