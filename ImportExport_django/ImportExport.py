from import_export.admin import ImportExportModelAdmin

@admin.register(Objeto)
class ObjetooAdmin(ImportExportModelAdmin):
    resource_class =CatalogoResource
    list_display = Attr(Objeto)
    list_display_links = Attr(Objeto)