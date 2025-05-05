    
class Permissions:
    ADD_PRODUCT = 'add_product'
    VIEW_PRODUCT = 'view_product'
    EDIT_PRODUCT = 'edit_product'
    DELETE_PRODUCT = 'delete_product'
    VIEW_ORDERS = 'view_orders'
    PROCESS_ORDER = 'process_order'
    MANAGE_USERS = 'manage_users'

    CHOICES = [
        (ADD_PRODUCT, 'Add Product'),
        (VIEW_PRODUCT, 'View Product'),
        (EDIT_PRODUCT, 'Edit Product'),
        (DELETE_PRODUCT, 'Delete Product'),
        (VIEW_ORDERS, 'View Orders'),
        (PROCESS_ORDER, 'Process Order'),
        (MANAGE_USERS, 'Manage Users'),
    ]
