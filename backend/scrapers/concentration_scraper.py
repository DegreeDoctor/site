from PyPDF2 import PdfReader
import json

def convert_pdf_to_text(file_path):
  reader = PdfReader(file_path)
  pages_num = len(reader.pages)
  file_text = ""
  for pg_num in range(pages_num):
    page = reader.pages[pg_num]
    file_text += page.extract_text().strip()
  return file_text

def parse_course(c_str):
  # string clean up for inconsistent spacing after converting pdf->str
  if c_str.find("Last updated:") >= 0:
    c_str = c_str.split("Last updated:")[0]
  if (not c_str[4] == " ") and c_str[3] == " ":
    c_str = c_str[0:3] + c_str[4] + " " + c_str[6:]
  if c_str[9] == " " and c_str[10] == "/":
    c_str = c_str[0:9] + c_str[10:]

  # Parse Course code and name
  or1, or2 = c_str.find("(or "), c_str.find("( or ")
  course_code = ""
  course_name = ""
  if or1 == -1 and or2 == -1:
    if c_str[9] == " ":
      course_code = c_str[0:9]
      course_name = c_str[10:]
    elif c_str[9] == "/":
      course_code = c_str[0:14]
      course_name = c_str[15:]
  else:
    y = c_str.find(")")
    if or1 >= 0:
      or_str = "(" + c_str[or1+1:y].strip() + ")"
      course_code = c_str[0:or1] + or_str
      course_name = c_str[y+1:]
    else:
      or_str = "(" + c_str[or2+1:y].strip() + ")"
      course_code = c_str[0:or2] + or_str
      course_name = c_str[y+1:]
  # Hardcoded rules on course names to be consistent with catalog and SIS
  if course_name == "ML for Bioinformatics ( Computational Biology )":
    course_name = "Mach Learning Bioinformatics"
  if course_name == "Introduction to Numerical Methods for Diff. Eqns.":
    course_name = "Introduction to Numerical Methods for Differential Equations"
  if course_name == "Application /Advanced Programming using Java":
    course_name = "Application Prog Using Java"
  # remove "-"
  if "Large -Scale" in course_name:
    course_name = course_name.replace("Large -Scale","LargeScale")
  if "L inear" in course_name:
    course_name = course_name.replace("L inear","Linear")
  if "Cyber -Physical" in course_name:
    course_name = course_name.replace("Cyber -Physical","CyberPhysical")
  # remove prefixes, abbreviations
  if "[CI]" in course_name:
    course_name = course_name.replace("[CI]","")
  if "(phased out" in course_name:
    course_name = course_name[0:course_name.find("(phased out")]
  if "(MBE)" in course_name:
    course_name = course_name.replace("(MBE)","")
  if "(CCN)" in course_name:
    course_name = course_name.replace("(CCN)","")
  if "(CHD)" in course_name:
    course_name = course_name.replace("(CHD)","")
  if "(ACHD)" in course_name:
    course_name = course_name.replace("(ACHD)","")
  if "(MPS)" in course_name:
    course_name = course_name.replace("(MPS)","")

  if course_name == "Parallel Programming /Parallel Computing":
    course_name = ["Parallel Programming", "Parallel Computing"]
  else:
    course_name = [course_name.strip()]
  # print(course_name," "*(50-len(course_name)), "|", course_code)
  return (course_code.strip(), course_name)



file_text = convert_pdf_to_text("../template_files/csci-concentration-courses.pdf")
file_text = file_text.strip().split('\n')
itr = 0
while itr < len(file_text):
  if file_text[itr].find("Concentration Area:") >= 0:
    break
  itr += 1

concentration_dict = dict()
curr_concentration = ""
for i in range(itr, len(file_text)):
  line = file_text[i]
  if line.find("Concentration Area:") >= 0:
    curr_concentration = line.split("Concentration Area:")[1]
    curr_concentration = " ".join(curr_concentration.split())
    if curr_concentration not in concentration_dict:
      concentration_dict[curr_concentration] = []
  else:
    line = " ".join(line.split())
    ccode, cname = parse_course(line)
    concentration_dict[curr_concentration].extend(cname)

json_object = json.dumps(concentration_dict)
with open("../data/csci-concentration.json", "w") as outfile:
  outfile.write(json_object)
