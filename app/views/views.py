from django.http import FileResponse
from .create import *
from .delete import *
from .edit import *
from .detail import *
from .list import *
from .dashboard import *


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'app/base/index.html')


class FileView(View):
    def get(self, request, typ, pk):
        if typ == 'course_img':
            course = get_object_or_404(Course, pk=pk)
            return FileResponse(open(course.image.url[1:], 'rb'), as_attachment=True)
        elif typ == 'profile_img':
            profile = get_object_or_404(User, pk=pk)
            return FileResponse(open(profile.image.url[1:], 'rb'), as_attachment=True)
        elif typ == 'announcement_img':
            announcement = get_object_or_404(Announcement, pk=pk)
            return FileResponse(open(announcement.image.url[1:], 'rb'), as_attachment=True)
        else:
            pass
