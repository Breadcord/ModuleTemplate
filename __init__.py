import breadcord


class ModuleCogClassName(breadcord.module.ModuleCog):
    def __init__(self):
        super().__init__("module_id")


async def setup(bot: breadcord.Bot):
    await bot.add_cog(ModuleCogClassName())
