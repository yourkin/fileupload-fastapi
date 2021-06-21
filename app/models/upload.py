from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Upload(models.Model):
    filename = fields.TextField()
    sha1 = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.filename


UploadSchema = pydantic_model_creator(Upload)
