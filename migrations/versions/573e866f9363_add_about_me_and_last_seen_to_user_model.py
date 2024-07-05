"""Add about_me and last_seen to User model

Revision ID: 573e866f9363
Revises: 52f61c29a35d
Create Date: 2024-07-04 21:25:25.240317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573e866f9363'
down_revision = '52f61c29a35d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.TEXT(),
               type_=sa.String(length=140),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.String(length=140),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
