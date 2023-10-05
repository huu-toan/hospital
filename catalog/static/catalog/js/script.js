function toggleMenu() {
    const navList = document.querySelector('.nav-list');
    navList.classList.toggle('active');
}
function _NewListDocter_NewListDocterPortlet_INSTANCE_lmfb_submitForm(curParam, cur) {
    var data = {};

    data[curParam] = cur;

    Liferay.Util.postForm(
        document.bfkt__NewListDocter_NewListDocterPortlet_INSTANCE_lmfb_pageIteratorFm,
        {
            data: data
        }
    );
}