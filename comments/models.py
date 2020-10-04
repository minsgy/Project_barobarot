from django.db import models
# Comment 
class Comment(models.Model):
    title = models.CharField(max_length=20) # 댓글 제목
    content = models.TextField() # 댓글 내용
    engineer = models.ForeignKey("engineers.Engineer", related_name="comments", on_delete=models.CASCADE) # 연결된 기사
    user = models.ForeignKey("users.User", related_name="comments", on_delete=models.CASCADE) # 댓글 작성자
    
    def __str__(self):
        return self.title