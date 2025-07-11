<<<<<<< HEAD
/*global opener */
'use strict';
{
    const initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
}
=======
(function() {

    'use strict';

    var windowRef = window;
    var windowRefProxy;
    var windowName, widgetName;
    var openerRef = windowRef.opener;
    if (!openerRef) {
        // related modal is active
        openerRef = windowRef.parent;
        windowName = windowRef.name;
        widgetName = windowName.replace(/^(change|add|delete|lookup)_/, '');
        windowRefProxy = {
            name: widgetName,
            location: windowRef.location,
            close: function() {
                openerRef.dismissRelatedObjectModal();
            }
        };
        windowRef = windowRefProxy;
    }

    // default django popup_response.js
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch (initData.action) {
        case 'change':
            if (typeof(openerRef.dismissChangeRelatedObjectPopup) === 'function') {
                openerRef.dismissChangeRelatedObjectPopup(windowRef, initData.value, initData.obj, initData.new_value);
            }
            break;
        case 'delete':
            if (typeof(openerRef.dismissDeleteRelatedObjectPopup) === 'function') {
                openerRef.dismissDeleteRelatedObjectPopup(windowRef, initData.value);
            }
            break;
        default:
            if (typeof(openerRef.dismissAddRelatedObjectPopup) === 'function') {
                openerRef.dismissAddRelatedObjectPopup(windowRef, initData.value, initData.obj);
            }
            break;
    }

})();
>>>>>>> 7f246f6795f13c1deb8e26559e17f430df061c0d
