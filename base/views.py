from .models import *

from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
import fitz, base64, os


# Create your views here.

def highlight_pdf(input_path, output_path, search_term):
    doc = fitz.open(input_path)
    for page in doc:
        found = page.search_for(search_term)
        for inst in found:
            highlight = page.add_highlight_annot(inst)
            highlight.update()
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()

@api_view(['GET'])
def index(request):
    print("here")

    return Response({'msg':"i am awake"}, status = 200)


@api_view(['POST'])
def highlight(request):
    data = request.data
    if not data['pdf']:
        return Response({"msg":"PDF file not uploaded."},status = 400)
    if not data['search']:
        return Response({"msg":"No value to search"},status = 400)
    
    uri = data['pdf']['uri']
    if "," in uri:
        uri = uri.split(",")[1]

    file = base64.b64decode(uri)

    input_path = os.path.join(settings.MEDIA_ROOT , data['pdf']['name'])
    with open(input_path, 'wb') as f:
            f.write(file)

    # Highlight and save to output
    output_filename = f"highlighted_{data['pdf']['name']}"
    output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
    highlight_pdf(input_path, output_path, data['search'])

    # Convert result to base64
    with open(output_path, 'rb') as f:
        result_base64 = base64.b64encode(f.read()).decode('utf-8')

    # Clean up
    os.remove(input_path)
    
    
    return Response({"result": result_base64}, status = 200)

