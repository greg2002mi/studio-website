from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
# 15 dashboard
    path("dashboard", views.dashboard, name="dashboard"),
    # ---------- edit orders ----------
    path("edit_order/<int:ordid>", views.edit_o, name="edit_order"),
    path("edit_call/<int:ordid>", views.e_call, name="edit_call"),
    path("order_pr/<int:ordid>/<int:s>", views.o_pr, name="order_pr"),
    path("call_pr/<int:ordid>/<int:s>", views.c_pr, name="call_pr"),
    # ---------- edit reviews ----------
    path("delete_rw/<int:entry>", views.d_rw, name="delete_rw"),
    path("managereview", views.managereview, name="managereview"),
    # ---------- header ----------
    path("manageheader", views.manageheader, name="manageheader"),
    path("new_he", views.n_he, name="new_he"),
    path("edit_he/<int:entry>", views.e_he, name="edit_he"),
    path("delete_he/<int:entry>", views.d_he, name="delete_he"),
    # ---------- vcategory ----------
    path("managevideocat", views.managevideocat, name="managevideocat"),
    path("new_vcat", views.n_vcat, name="new_vcat"),
    path("edit_vcat/<int:entry>", views.e_vcat, name="edit_vcat"),
    path("delete_vcat/<int:entry>", views.d_vcat, name="delete_vcat"),
    # ---------- video case ----------
    path("managevideocase", views.managevideocase, name="managevideocase"),
    path("new_vc", views.n_vc, name="new_vc"),
    path("new_vc2", views.n_vc2, name="new_vc2"), # to first create category before saving the video case
    path("edit_vc/<int:entry>", views.e_vc, name="edit_vc"),
    path("delete_vc/<int:entry>", views.d_vc, name="delete_vc"),
    # ---------- reel category ----------
    path("managereelcat", views.managereelcat, name="managereelcat"),
    path("new_rcat", views.n_rcat, name="new_rcat"),
    path("edit_rcat/<int:entry>", views.e_rcat, name="edit_rcat"),
    path("delete_rcat/<int:entry>", views.d_rcat, name="delete_rcat"),
    # ---------- reel ----------
    path("managereel", views.managereel, name="managereel"),
    path("new_reel", views.n_reel, name="new_reel"),
    path("new_reel2", views.n_reel2, name="new_reel2"), # to first create category before saving a reel
    path("edit_reel/<int:entry>", views.e_reel, name="edit_reel"),
    path("delete_reel/<int:entry>", views.d_reel, name="delete_reel"),
    # ---------- icategory ----------
    path("manageimgcat", views.manageimgcat, name="manageimgcat"),
    path("new_icat", views.n_icat, name="new_icat"),
    path("edit_icat/<int:entry>", views.e_icat, name="edit_icat"),
    path("delete_icat/<int:entry>", views.d_icat, name="delete_icat"),
    # ---------- Image ----------
    path("manageimage", views.manageimage, name="manageimage"),
    path("new_i", views.n_i, name="new_i"),
    path("new_i2", views.n_i2, name="new_i2"), # to first create category before saving an image
    path("edit_i/<int:entry>", views.e_i, name="edit_i"),
    path("delete_i/<int:entry>", views.d_i, name="delete_i"),
    # ---------- Gfx ----------
    path("managegfx", views.managegfx, name="managegfx"),
    path("new_g", views.n_g, name="new_g"),
    path("edit_g/<int:entry>", views.e_g, name="edit_g"),
    path("delete_g/<int:entry>", views.d_g, name="delete_g"),
    # ---------- Website design ----------
    path("manageweb", views.manageweb, name="manageweb"),
    path("new_w", views.n_w, name="new_w"),
    path("edit_w/<int:entry>", views.e_w, name="edit_w"),
    path("delete_w/<int:entry>", views.d_w, name="delete_w"),
    # ---------- SMM ----------
    path("managesmm", views.managesmm, name="managesmm"),
    path("new_s", views.n_s, name="new_s"),
    path("edit_s/<int:entry>", views.e_s, name="edit_s"),
    path("delete_s/<int:entry>", views.d_s, name="delete_s"),
    # ---------- EgSMM ----------
    path("manageegsmm", views.manageegsmm, name="manageegsmm"),
    path("new_es", views.n_es, name="new_es"),
    path("edit_es/<int:entry>", views.e_es, name="edit_es"),
    path("delete_es/<int:entry>", views.d_es, name="delete_es"),
    # ---------- Services ----------
    path("manageserv", views.manageserv, name="manageserv"),
    path("new_serv", views.n_serv, name="new_serv"),
    path("edit_serv/<int:entry>", views.e_serv, name="edit_serv"),
    path("delete_serv/<int:entry>", views.d_serv, name="delete_serv"),
    # ---------- Clients ----------
    path("manageclient", views.manageclient, name="manageclient"),
    path("new_cl", views.n_cl, name="new_cl"),
    path("edit_cl/<int:entry>", views.e_cl, name="edit_cl"),
    path("delete_cl/<int:entry>", views.d_cl, name="delete_cl"),
    # ---------- Aboutus ----------
    path("manageaboutus", views.manageaboutus, name="manageaboutus"),
    path("new_au", views.n_au, name="new_au"),
    path("edit_au/<int:entry>", views.e_au, name="edit_au"),
    path("delete_au/<int:entry>", views.d_au, name="delete_au"),
    # ---------- Contactus ----------
    path("managecontactus", views.managecontactus, name="managecontactus"),
    path("new_ct", views.n_ct, name="new_ct"),
    path("edit_ct/<int:entry>", views.e_ct, name="edit_ct"),
    path("delete_ct/<int:entry>", views.d_ct, name="delete_ct"),
    # ---------- Main vids and services ----------
    path("managemain", views.managemain, name="managemain"),
    path("new_vs", views.n_vs, name="new_vs"),
    path("edit_vs/<int:entry>", views.e_vs, name="edit_vs"),
    path("delete_vs/<int:entry>", views.d_vs, name="delete_vs"),
    path("new_fw", views.n_fw, name="new_fw"),
    path("edit_fw/<int:entry>", views.e_fw, name="edit_fw"),
    path("delete_fw/<int:entry>", views.d_fw, name="delete_fw"),
    path("new_wd", views.n_wd, name="new_wd"),
    path("edit_wd/<int:entry>", views.e_wd, name="edit_wd"),
    path("delete_wd/<int:entry>", views.d_wd, name="delete_wd"),
    ]