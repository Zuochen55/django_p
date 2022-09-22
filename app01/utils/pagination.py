from django.utils.safestring import mark_safe
class Pagination:

    def __init__(self, request, queryset, page_param="page", page_size=3, plus=2):
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        total_page = queryset.count()
        total_page_count, div = divmod(total_page, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        if self.page <= self.plus:
            start_page = 1
            end_page = 2 * self.plus + 1

        elif self.page + self.plus > self.total_page_count:
            start_page = self.total_page_count - 2 * self.plus
            end_page = self.total_page_count
        else:
            start_page = self.page - self.plus
            end_page = self.page + self.plus

        page_list = []

        page_list.append(
            '<li><a href="?page={}"><span class="glyphicon glyphicon-step-backward" aria-hidden="true"></span></a></li>'.format(
                1))

        if self.page > 1:
            page_list.append(
                '<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span></a></li>'.format(
                    self.page - 1))
        else:
            page_list.append(
                '<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span></a></li>'.format(
                    1))

        for i in range(start_page, end_page + 1):
            if i == self.page:
                element = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
            else:
                element = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_list.append(element)

        if self.page < self.total_page_count:
            page_list.append(
                '<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span></a></li>'.format(
                    self.page + 1))
        else:
            page_list.append(
                '<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span></a></li>'.format(
                    self.total_page_count))

        page_list.append(
            '<li><a href="?page={}"><span class="glyphicon glyphicon-step-forward" aria-hidden="true"></span></a></li>'.format(
                self.total_page_count))
        page_string = mark_safe("".join(page_list))
        return page_string


