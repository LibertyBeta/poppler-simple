import Options


srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'


def set_options(opt):
    opt.tool_options('compiler_cxx')


def configure(conf):
    conf.check_tool('compiler_cxx')
    conf.check_tool('node_addon')

    conf.check_cfg(package='poppler', args='--cflags --libs', mandatory=True)


def build(bld):
    obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
    obj.cxxflags = ['-rdynamic']
    obj.target = 'poppler'
    obj.source = './src/NodePopplerDocument.cc ./src/NodePopplerPage.cc ./src/iconv_string.cc'
    obj.uselib = ['GDK-3.0', 'POPPLER', 'POPPLER-GLIB']
