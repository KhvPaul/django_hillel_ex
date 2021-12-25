from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('contact', views.contact_form, name='contact_form'),

    path('triangle', views.triangle_form, name='triangle_form'),

    path('persons/', views.PersonListView.as_view(), name='persons'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('person/create/', views.PersonCreate.as_view(), name='person-create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person-update'),

    # path('person/add/', views.add_person, name='person-add'),   # Специально для instance
]
