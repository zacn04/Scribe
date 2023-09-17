from image_to_latex import image_to_latex
from latex_to_response import latex_parsing
from latex_to_response import result_handling
from handwriting import main
import json

<<<<<<< HEAD
def hand_to_hand(x : str):
=======
def hand_to_hand(x):
>>>>>>> 9125d73 (tys first commit)
  latex = image_to_latex.image_to_latex(x) # x is the path of the image in a string
  text_query = latex_parsing.latex_to_text(latex)
  json_answer = result_handling.request_query_response(text_query)
  with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(json_answer["queryresult"], indent=4))
  text_answer = result_handling.parse(json_answer)
  print(text_answer)
  hand = main.process_text_to_image(text_answer) #Function will generate an image that is passed back
  return hand

<<<<<<< HEAD
if __name__ == "__main__":
  answer = hand_to_hand("image_to_latex/test2.png")
  answer.save("test_answer.png")
=======
# answer = hand_to_hand("image_to_latex/test2.png")
# answer.save("test_answer.png")
>>>>>>> 9125d73 (tys first commit)
