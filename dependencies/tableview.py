class Table(object):
    """
    The table renders a table with sortable columns etc.
    It is meant to be subclassed to provide methods for getting specific table
    info.
    """

    def __init__(self, request, base_url, view_url, items,
                 show_sort_column=False, buttons=None, pagesize=20,
                 show_select_column=True, show_size_column=True,
                 show_modified_column=True, show_status_column=True):
        pass
    
    def msg_select_item(self, item):
        pass

    def within_batch_size(self):
        pass

    def set_checked(self, item):
        pass

    
    def batch(self):
        pass

    def batching(self):
        pass

    def _get_select_currentbatch(self):
        pass

    def _set_select_currentbatch(self, value):
        pass

    def _get_select_all(self):
        pass

    def _set_select_all(self, value):
        pass

    def show_select_all_items(self):
        pass

    def get_nosort_class(self):
        """
        """
        pass

    def selectall_url(self):
        pass

    def selectscreen_url(self):
        pass

    def selectnone_url(self):
        pass

    def show_all_url(self):
        pass

    def selected(self, item):
        pass

    def viewname(self):
        return self.view_url.split('?')[0].split('/')[-1]

    def quote_plus(self, string):
        pass