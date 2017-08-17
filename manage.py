#  ### 专门写脚本命令###
from flask_script import Manager
# 数据库生成迁移表 和数据库迁
from flask_migrate import MigrateCommand, Migrate
from exts import db
# manage 初始化需要用到app
from zlkt import app
# 导入用户模型 用来进行迁移映射
from models import User, Question


# 初始化manager
manager = Manager(app)


# 使用migrate绑定app和db
migrate = Migrate(app, db)


# 添加迁移脚本的命令到脚本中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()