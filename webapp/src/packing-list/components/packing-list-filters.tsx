import { SelectInput } from "react-admin";
import { PackingListStatusChoices } from "../values/packing-list-status-choices";

export const PackingListFilters = [
  <SelectInput source="status" choices={PackingListStatusChoices} />,
];
