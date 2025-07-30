from sqladmin import ModelView

from src.orders.models.sqlalchemy import Basket, BasketLine, Order, OrderLine


class BasketAdmin(ModelView, model=Basket):
    category = "Orders"
    icon = "fa-solid fa-shopping-basket"
    name = "Basket"
    name_plural = "Baskets"
    
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id, Basket.status]
    column_sortable_list = [Basket.id, Basket.price, Basket.status]


class BasketLineAdmin(ModelView, model=BasketLine):
    category = "Orders"
    icon = "fa-solid fa-list"
    name = "Basket Line"
    name_plural = "Basket Lines"
    
    column_list = [BasketLine.id, BasketLine.basket_id, BasketLine.product_id, BasketLine.quantity, BasketLine.price]
    column_searchable_list = [BasketLine.basket_id, BasketLine.product_id]
    column_sortable_list = [BasketLine.id, BasketLine.quantity, BasketLine.price]


class OrderAdmin(ModelView, model=Order):
    category = "Orders"
    icon = "fa-solid fa-receipt"
    name = "Order"
    name_plural = "Orders"
    
    column_list = [Order.id, Order.number, Order.user_id, Order.total_price, Order.status, Order.created_at]
    column_searchable_list = [Order.number, Order.user_id, Order.status]
    column_sortable_list = [Order.id, Order.number, Order.total_price, Order.created_at]


class OrderLineAdmin(ModelView, model=OrderLine):
    category = "Orders"
    icon = "fa-solid fa-clipboard-list"
    name = "Order Line"
    name_plural = "Order Lines"
    
    column_list = [OrderLine.id, OrderLine.order_id, OrderLine.product_id, OrderLine.quantity, OrderLine.price]
    column_searchable_list = [OrderLine.order_id, OrderLine.product_id]
    column_sortable_list = [OrderLine.id, OrderLine.quantity, OrderLine.price]


def register_orders_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(OrderLineAdmin)