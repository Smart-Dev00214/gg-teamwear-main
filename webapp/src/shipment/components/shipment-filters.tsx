import { SelectInput } from "react-admin";
import { ShipmentStatusChoices } from "../values/shipment-status-choices";

export const ShipmentFilters = [
  <SelectInput source="status" choices={ShipmentStatusChoices} />,
];
