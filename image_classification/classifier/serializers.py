from rest_framework import serializers


class ImageClassifierRequestSerializer(serializers.Serializer):
    image_path = serializers.CharField()

    def validate_image_path(self, image_path):
        if not any(image_path.endswith(extension) for extension in ["jpg", "jpeg", "png"]):
            raise serializers.ValidationError("Image path is not image.")
