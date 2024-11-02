# from django.db import models
# from django.contrib.auth.models import User




# class TODOO(models.Model):
#     srno=models.AutoField(auto_created=True,primary_key=True)
#     title= models.CharField(max_length=25)
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=False,blank=True,)
#     user = models.ForeignKey( User, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):
    """
    TODOO Model represents a to-do task with a title, status, 
    creation date, and an associated user. Each task belongs to 
    a user, and the user can manage tasks independently.
    
    Fields:
        - srno: Auto-incremented unique identifier for each task.
        - title: Title or short description of the task.
        - date: The timestamp when the task is created.
        - status: Boolean indicating completion status of the task.
        - user: ForeignKey linking the task to a specific user.
    """
    srno = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Auto-incremented primary key for each task"
    )
    title = models.CharField(
        max_length=25,
        help_text="Short title or description of the task (max 25 characters)"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp of when the task was created"
    )
    status = models.BooleanField(
        default=False,
        blank=True,
        help_text="Completion status of the task (True for completed)"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User associated with this task"
    )

    def __str__(self):
        """
        Returns a string representation of the TODOO object, 
        showing the title and user for better readability.
        """
        return f"{self.title} - {self.user.username}"

    class Meta:
        """
        Meta options to specify ordering of tasks by creation date.
        """
        ordering = ['-date']
        verbose_name = "To-Do Task"
        verbose_name_plural = "To-Do Tasks"
