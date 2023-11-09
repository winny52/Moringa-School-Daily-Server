"""Update models

Revision ID: 5b3225acc6a1
Revises: ccdf021dafe4
Create Date: 2023-11-02 12:56:18.025485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b3225acc6a1'
down_revision = 'ccdf021dafe4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('media_url', sa.String(length=255), nullable=True))
        batch_op.drop_column('video_url')
        batch_op.drop_column('image_thumbnail')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_thumbnail', sa.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('video_url', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('media_url')

    # ### end Alembic commands ###