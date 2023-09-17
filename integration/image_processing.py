from image_to_latex import image_to_latex
from latex_to_response import *

def hand_to_hand(x : str) -> None:
  text = image_to_text(x)
  text2 = parse(request_query_response(text))
  hand = text_to_handwriting(your_handwriting, text2) #Function will generate an image that is passed back
  return hand
