'''
Usage:
    copy.py [backup] [restore] [copy]
'''

import os
import sys
import shutil
import logging

thisdir = os.path.dirname(__file__)

from lib.bashlog import getlogger

logger = logging.getLogger()

class Copier(object):

    def __init__(self, sorcedir, targetdir):
        logger.debug('sorce: %s; target: %s', sorcedir, targetdir)

        self.source_dir = sorcedir
        self.source_icons = self._icons(sourcedir)

        self.target_dir = targetdir
        self.target_icons = self._icons(targetdir)

    def backup(self):
        total = failed = 0
        for common in self.source_icons.intersection(self.target_icons):
            total += 1
            old = os.path.join(self.target_dir, common)
            new = os.path.join(self.target_dir, '.'+common)
            if not self._replace(old, new):
                failed += 1
                logger.error('backup failed %s', common)
        if failed != 0:
            logger.error('backup complete %s/%s', total - failed, total)
        else:
            logger.info('backup complete')

    def restore(self):
        total = failed = 0
        for dotfile in (x for x in self.target_icons if x.startswith('.')):
            total += 1
            old = os.path.join(self.target_dir, docfile)
            new = os.path.join(self.target_dir, docfile[1:])

            if not self._replace(old, new):
                failed += 1
                logger.error('restore failed %s', docopt)

        if failed != 0:
            logger.error('restore complete %s/%s', total - failed, total)
        else:
            logger.info('restore complete')

    def copy(self):
        total = failed = 0
        for common in self.source_icons.intersection(self.target_icons):
            total += 1
            src = os.path.join(self.source_dir, common)
            if not self._replace(src, self.target_dir):
                failed += 1
                logger.error('copy failed %s', common)

        if failed != 0:
            logger.error('copy complete %s/%s', total - failed, total)
        else:
            logger.info('copy complete')

    def _replace(self, old, new):
        try:
            shutil.copy2(old, new)
        except BaseException as e:
            logger.error('replace %s failed: %s', old, e)
            return False
        else:
            logger.debug('replace %s finished', old)
            return True

    def _icons(self, path):
        icons = set()
        for _, _, files in os.walk(path):
            icons.update(x for x in files if x.endswith('.png'))
        return icons

if __name__ == '__main__':
    targetdir = '/var/lib/apkd'
    sourcedir = os.path.normpath(os.path.join(__file__, '..', 'apkd'))

    copier = Copier(sourcedir, targetdir)

    getlogger(logger, logging.DEBUG)

    if len(sys.argv) == 1:
        sys.argv.extend(('backup', 'copy'))

    for each in sys.argv[1:]:
        if each == 'backup':
            copier.backup()
        elif each == 'restore':
            copier.restore()
        elif each == 'copy':
            copier.copy()
        else:
            logger.error('unknown argv %s', each)
