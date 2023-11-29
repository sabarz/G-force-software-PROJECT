from django.urls import path
from . import views
## when we use ModelViewSet we should implement urls with routers
from rest_framework_nested import routers as nested
from rest_framework import routers 


nestedRouter = nested.DefaultRouter()
router = routers.SimpleRouter()

### account info urls
router.register('profile',views.MemberProfileView,basename='profile')
router.register('home',views.HomeAccountView,basename='home')
router.register('change',views.ChangePasswordView,basename='change')

### workspace urls
router.register('workspace',views.WorkspaceView,basename='workspace')
router.register('crworkspace',views.CreateWorkspaceView,basename='crworkspace')

### board urls
router.register('board',views.BoardView,basename='board')
router.register('board-bgimage',views.BoardImageView,basename='board-bgimage')
router.register('boards-has-start',views.BoardStarView,basename='boards-has-start')
router.register('board-star-update',views.BoardStarUpdate,basename='board-star-update')
router.register('board-invitation-link',views.BoardInvitationLinkView,basename='board-invitation-link')
router.register('starred-boards',views.BoardStarView,basename='starred-boards')
router.register('star',views.BoardStarUpdate,basename='star')
router.register('crboard',views.CreateBoardView,basename='crboard')
router.register('recentlyviewed',views.BoardRecentlyViewedView,basename='recentlyviewed')
router.register('board-labels',views.LabelBoardView,basename='board-labels')

### invite member to board
router.register('board-member',views.BoardMembersView,basename='board-member')
router.register('invite',views.InviteMemberView,basename='invite')
router.register('user-search',views.FindUserView,basename='user-search')

### list urls
router.register('list',views.ListView,basename='list')
router.register('crlist',views.CreateListView,basename='crlist')


### card details urls
router.register('card',views.CardView,basename='card')
router.register('crcard',views.CreateCardView,basename='crcard')
router.register('checklist',views.CardChecklistView,basename='checklist')
router.register('crchecklist',views.CreateChecklistView,basename='crchecklist')
router.register('critem',views.CreateItemView,basename='critem')
router.register('crlabel',views.CreateLabelView,basename='crlabel')
router.register('crcard-labels',views.LabelCardAssignView,basename='crcard-labels')
router.register('card-labels',views.LabelCardView,basename='card-labels')
router.register('assign',views.CardAssignmentView,basename='assign')
router.register('dnd',views.Internal_DndView,basename='dnd')

### timeline urls
router.register('list-tl',views.ListTimelineView,basename='list-tl')
router.register('member-tl',views.MemberTimelineView,basename='member-tl')
router.register('label-tl',views.LabelTimelineView,basename='label-tl')



###
router.register('calender',views.CalenderView,basename='calender')



### workspace urls
router.register('workspace',views.WorkspaceView,basename='workspace')
router.register('crworkspace',views.CreateWorkspaceView,basename='crworkspace')

### board urls
router.register('board',views.BoardView,basename='board')
router.register('board-bgimage',views.BoardImageView,basename='board-bgimage')
router.register('boards-has-start',views.BoardStarView,basename='boards-has-start')
router.register('board-star-update',views.BoardStarUpdate,basename='board-star-update')
router.register('board-invitation-link',views.BoardInvitationLinkView,basename='board-invitation-link')
router.register('starred-boards',views.BoardStarView,basename='starred-boards')
router.register('star',views.BoardStarUpdate,basename='star')
router.register('crboard',views.CreateBoardView,basename='crboard')
router.register('recentlyviewed',views.BoardRecentlyViewedView,basename='recentlyviewed')
router.register('board-labels',views.LabelBoardView,basename='board-labels')

### invite member to board
router.register('board-member',views.BoardMembersView,basename='board-member')
router.register('invite',views.InviteMemberView,basename='invite')
router.register('user-search',views.FindUserView,basename='user-search')

### list urls
router.register('list',views.ListView,basename='list')
router.register('crlist',views.CreateListView,basename='crlist')


### card details urls
router.register('card',views.CardView,basename='card')
router.register('crcard',views.CreateCardView,basename='crcard')
router.register('checklist',views.CardChecklistView,basename='checklist')
router.register('crchecklist',views.CreateChecklistView,basename='crchecklist')
router.register('critem',views.CreateItemView,basename='critem')
router.register('crlabel',views.CreateLabelView,basename='crlabel')
router.register('crcard-labels',views.LabelCardAssignView,basename='crcard-labels')
router.register('card-labels',views.LabelCardView,basename='card-labels')
router.register('assign',views.CardAssignmentView,basename='assign')
router.register('dnd',views.Internal_DndView,basename='dnd')

### timeline urls
router.register('list-tl',views.ListTimelineView,basename='list-tl')
router.register('member-tl',views.MemberTimelineView,basename='member-tl')
router.register('label-tl',views.LabelTimelineView,basename='label-tl')

### burndown
router.register('burndown-chart', views.BurndownChartViewSet, basename='burndown-chart')

###
router.register('calender',views.CalenderView,basename='calender')


urlpatterns = router.urls