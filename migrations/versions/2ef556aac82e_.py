"""empty message

Revision ID: 2ef556aac82e
Revises: 224c36875099
Create Date: 2024-07-14 15:15:49.122242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ef556aac82e'
down_revision = '224c36875099'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_club_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_club_id'], ['book_club.id'], name=op.f('fk_comment_book_club_id_book_club')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_comment_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
