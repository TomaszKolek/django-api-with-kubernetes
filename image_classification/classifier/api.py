from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from classifier.serializers import ImageClassifierRequestSerializer
from classifier.image_classifier import ImageClassifier



class GetAttributesApi(RetrieveAPIView):
    serializer_class = ImageClassifierRequestSerializer

    def get(self, request, *args, **kwargs):
        request_serializer = ImageClassifierRequestSerializer(data=request.GET)
        if request_serializer.is_valid(raise_exception=True):
            image_path = request_serializer.validated_data["image_path"]
            response = {"image": image_path}
            response.update(ImageClassifier(image_path).get_attributes())
            return Response(response, status=200)

        return Response("Image path is malformed", status=400)
