import re


line = "	>	> NAME: Nord Stream 2: Wolfgang Schäuble kritisiert Ostsee-Pipeline"
line1 = ">	> NAME: Wrangelsburg: Klimaaktivisten besetzen Pipelinebaustelle"
line2 = "===================================================================================================="
regex_name = r"\s*\=*\>*\s*\s*\=*\>*\s*\s*\=*\>*\s*[NAME:]*\s+(.*)"
# regex_name = r"(.*)"

if re.findall(regex_name, line):
    print("Yes")
else:
    print("No")
