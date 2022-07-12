from __future__ import annotations


class Document():
    _state = None
    
    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        self._state = state
        self._state.context = self
        print(f"\nI'm in a {self._state.__class__.__name__[:-5]} state!")

    def get_approved(self, is_approved: bool) -> None:
        self._state.get_approved(is_approved)

    def get_expired(self, is_expired: bool) -> None:
        self._state.get_expired(is_expired)

    def get_published(self, is_admin: bool) -> None:
        self._state.get_published(is_admin)


class State():
    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, document: Document) -> None:
        self._document = document

    def get_approved(self, is_approved: bool) -> None:
        print("You are not allowed to do that in this state!")

    def get_expired(self, is_expired: bool) -> None:
        print("You are not allowed to do that in this state!")

    def get_published(self, is_admin: bool) -> None:
        print("You are not allowed to do that in this state!")
        
    
class DraftState(State):
    def get_published(self, is_admin: bool) -> None:
        if is_admin:
            print("Document was made by admin and is directly published")
            self.context.transition_to(PublishedState())
        else:
            print("Document was made by user and goes to moderation before publishing")
            self.context.transition_to(ModerationState())


class ModerationState(State):
    def get_approved(self, is_approved: bool) -> None:
        if is_approved:
            print("Document was approved and published")
            self.context.transition_to(PublishedState())
        else:
            print("Document wasn't approved so it goes back to draft")
            self.context.transition_to(ModerationState())


class PublishedState(State):
    def get_expired(self, is_expired: bool) -> None:
        if is_expired:
            print("Document was expired, so it must go back to draft")
            self.context.transition_to(DraftState())
        else:
            print("Document wasn't expired, all in order =)")
            self.context.transition_to(PublishedState())


if __name__ == "__main__":
    document = Document(DraftState())
    document.get_published(False)
    document.get_approved(True)
    document.get_expired(False)
    # Invalid action for current state
    document.get_approved(False)


""" OUTPUT
I'm in a Draft state!
Document was made by user and goes to moderation before publishing

I'm in a Moderation state!
Document was approved and published

I'm in a Published state!
Document wasn't expired, all in order =)

I'm in a Published state!
You are not allowed to do that in this state!
"""