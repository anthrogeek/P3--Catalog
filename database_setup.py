import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	email = Column(String(250), nullable = False)
	picture = Column(String(250))


class Genre(Base):
	__tablename__ = 'genre'
	
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)


class BookItem(Base):
	__tablename__ = 'book_item'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	author = Column(String(250))
	genre_id = Column(Integer, ForeignKey('genre.id'))
	genre = relationship(Genre)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)


	



	@property
	def serialize(self):
		#Returns object data in an easily serialized format
		return {
			'name' : self.name,
			'description' : self.description,
			'price' : self.price,
			'author' : self.author,
			'id' : self.id,
			'genre' : self.genre.name,
		}



engine = create_engine(
'sqlite:///bookswithusers.db')

Base.metadata.create_all(engine)