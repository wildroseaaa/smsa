from sqlalchemy import Column, Integer, DateTime, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime 


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name_tm = Column(String)
    name_ru = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    category_subcategory = relationship('subCategory', backref='subcategory_category')

class Category(Base):
    __tablename__ = 'sub_category'
    id = Column(Integer, primary_key=True, index=True)
    name_tm = Column(String)
    name_ru = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)  

    subcategory_category = relationship('Category', back_populates='')