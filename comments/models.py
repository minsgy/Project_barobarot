from django.db import models
from core import models as core_models

# Comment 
class Comment(core_models.TimeStampedModel):
    content = models.TextField() # 댓글 내용
    engineer = models.ForeignKey("engineers.Engineer", related_name="comments", on_delete=models.CASCADE) # 연결된 기사
    user = models.ForeignKey("users.User", related_name="comments", on_delete=models.CASCADE) # 댓글 작성자

    # 댓글 작성 시간
    created_time = core_models.TimeStampedModel.created # Y.m.d
