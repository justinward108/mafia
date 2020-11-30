import logging

from mafia.constants import ALIGNMENT_MAFIA, CATEGORY_MAFIA_KILLING, CATEGORY_MAFIA_RANDOM
from mafia.mafialistener import MafiaListener, mafialistener
from mafia.role import Role
from mafia.mafiavote import MafiaVote

log = logging.getLogger("red.justinward.mafia.mafiagoon")


class MafiaGoon(Role):
    rand_choice = True
    town_balance = -6
    category = [CATEGORY_MAFIA_RANDOM, CATEGORY_MAFIA_KILLING]
    alignment = ALIGNMENT_MAFIA  # 1: Town, 2: Mafa, 3: Neutral
    channel_name = "werewolves"
    unique = False
    game_start_message = (
        "Your role is **Mafia**\n"
        "You win by killing everyone else in the village\n"
        "Lynch players during the day with `[p]ww vote <ID>`\n"
        "Vote to kill players at night with `[p]ww vote <ID>`"
    )

    async def see_alignment(self, source=None):
        """
        Interaction for investigative roles attempting
        to see team (Village, Mafia Other)
        """
        return ALIGNMENT_MAFIA

    async def get_role(self, source=None):
        """
        Interaction for powerful access of role
        Unlikely to be able to deceive this
        """
        return "MafiaGoon"

    async def see_role(self, source=None):
        """
        Interaction for investigative roles.
        More common to be able to deceive these roles
        """
        return "Mafia"

    @mafialistener("at_game_start", priority=2)
    async def _at_game_start(self):
        if self.channel_name:
            log.debug("Mafia has channel_name: " + self.channel_name)
            await self.game.register_channel(
                self.channel_name, self, MafiaVote
            )  # Add VoteGroup MafiaVote

        await self.player.send_dm(self.game_start_message)

    async def choose(self, ctx, data):
        """Handle night actions"""
        await self.player.member.send("Use `[p]ww vote` in your mafia channel")
