from django.db import models

class SoftDeleteModel(models.Model):

   deleted_at = models.DateTimeField('삭제일', null=True, default=None)  #각 테이블마다 붙힐 컬럼

   class Meta:
       abstract = True  #메타 옵션으로 추상 클래스를 이용하여 상속 이용 

   objects = SoftDeleteManager()  # 커스텀 매니저쓰...

   def delete(self, using=None, keep_parents=False):
       self.deleted_at = now()
       self.save(update_fields=['deleted_at'])

   def restore(self):  # 삭제된 레코드를 복구한다.
       self.deleted_at = None
       self.save(update_fields=['deleted_at'])

class SoftDeleteManager(models.Manager):
    use_for_related_fields = True  # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

#삭제된 객체 보기
MyModel.objects_with_deleted.last()
#영구 삭제 
m = MyModel.objects.last()
m.delete(True)