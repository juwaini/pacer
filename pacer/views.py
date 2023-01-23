from django.http import JsonResponse

from pacer.models import Score


def get_score(request, pk):
    try:
        data = Score.objects.get(user=pk)
        r = {'success': True, 'id': data.user.pk, 'score': data.score}
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)