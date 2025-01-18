
frappe.ui.Sidebar = class CustomSidebar extends frappe.ui.Sidebar{
    constructor(){
        super();
        this.changeStyle();
    }
    changeStyle(){
        frappe.db.get_doc("Owl Theme Settings", "Owl Theme Settings")
        .then(doc => {
            if (doc) {
                $(".body-sidebar").css("background-color", doc.sidebar_background_color);
                $(".standard-sidebar-item .sidebar-item-label").css("color", doc.sidebar_text_color);
            }
        }).catch(error => {
            console.error("Error details:", error);
        });
    }
}