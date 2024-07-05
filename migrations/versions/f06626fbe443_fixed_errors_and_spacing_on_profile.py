"""fixed errors and spacing on profile

Revision ID: f06626fbe443
Revises: cda38565d334
Create Date: 2024-07-04 23:17:18.012275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f06626fbe443'
down_revision = 'cda38565d334'
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
        batch_op.alter_column('password_hash',
               existing_type=sa.TEXT(),
               type_=sa.String(length=256),
               existing_nullable=True)
        batch_op.alter_column('about_me',
               existing_type=sa.VARCHAR(length=560),
               type_=sa.String(length=140),
               existing_nullable=True)
        batch_op.drop_column('profile_picture')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_picture', sa.VARCHAR(length=256), nullable=True))
        batch_op.alter_column('about_me',
               existing_type=sa.String(length=140),
               type_=sa.VARCHAR(length=560),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.TEXT(),
               existing_nullable=True)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.String(length=140),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
