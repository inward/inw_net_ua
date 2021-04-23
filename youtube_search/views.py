from django.shortcuts import render

from .forms import YoutubeForm
from .video import get_videos


def youtube(request):
    form = YoutubeForm()
    content = {}
    video_data = {}
    if request.method == 'POST':
        form = YoutubeForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data
            video_data = get_videos(content)
    print(video_data)

    return render(request, 'youtube_search/index.html', {'form': form.as_p(), 'content': content,
                                                         'video_data': video_data,})
