from alembic import op
import sqlalchemy as sa

from src.config import config

# revision identifiers, used by Alembic.
revision = '14b947b5df30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("sub", sa.String(36), primary_key=True),
    )


def downgrade():
    op.drop_table(
        "users"
    )
