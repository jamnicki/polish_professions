import os
import json


def main():
    prof_base_dict = {}
    for file in os.listdir("prof_lemas"):
        first_letter = file[0]
        with open(os.path.join("prof_lemas", file)) as f:
            txt = f.read()
        profession_bases = txt.split("|")

        prof_base_dict[first_letter.upper()] = [p.replace("\n", "").strip() for p in profession_bases]

    prof_base_dict = dict(sorted(prof_base_dict.items()))
    with open("profession_base.json", "w") as fw:
        json.dump(prof_base_dict, fw, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
