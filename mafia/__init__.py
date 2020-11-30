from .mafia import mafia


def setup(bot):
    bot.add_cog(mafia(bot))

__all__ = ["Seer", "Shifter", "VanillaWerewolf", "Villager"]
