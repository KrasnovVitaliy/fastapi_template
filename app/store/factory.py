from store.sample_store_abc import SampleStoreABC

from app.store.impl.inmemory_sample_store import InmemorySampleStore

available_sample_store_types = ["inmemory"]


class UnsuportedStoreError(Exception):
    """Unsupported store type exception.

    Args:
    ----
        Exception (_type_): _description_

    """


class StoreFactory:
    """Store factory."""

    def __init__(
        self,
        sample_store_type: str = "inmemory",
    ) -> None:
        """Init store factory.

        Args:
        ----
            sample_store_type (str, optional): Sample store type: ["inmemory"]. Defaults to "inmemory".

        Raises:
        ------
            UnsuportedStoreError: Unsupport user store type

        """
        self.sample_store_type = sample_store_type.lower()
        if self.sample_store_type not in available_sample_store_types:
            msg = "Unsupport sample store type: %s"
            raise UnsuportedStoreError(msg, self.sample_store_type)

    def sample_store(self) -> SampleStoreABC:
        """Get sample store imnplementation.

        Returns
        -------
            SampleStoreABC: Sample store implementation

        """
        if self.sample_store_type == "inmemory":
            return InmemorySampleStore()

        msg = "Unsupport sample store type: %s"
        raise UnsuportedStoreError(msg, self.users_store_type)
