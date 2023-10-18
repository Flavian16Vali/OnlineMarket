from django.shortcuts import render, get_object_or_404, redirect

from app1.models import Item
from conversation.forms import ConversationMessageForm
from conversation.models import Conversation


# Create your views here.
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.id_user == request.user.customuser:
        return redirect('app1:list_items')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.customuser.id])

    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user.customuser)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user.customuser
            conversation_message.save()

            return redirect('app1:list_items', pk=item_pk)
        else:
            form = ConversationMessageForm()

        return render(request, 'conversation/new_conversation.html', {'form': form})
